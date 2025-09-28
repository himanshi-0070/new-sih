
# Enhanced LCA Prediction Function - Optimized for 90%+ Accuracy
import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import PolynomialFeatures
import warnings
warnings.filterwarnings('ignore')

class OptimizedLCAPredictor:
    def __init__(self, model_path=None):
        if model_path is None:
            model_path = 'models/final_optimized_lca_model.pkl'

        try:
            self.model_components = joblib.load(model_path)
            self.metadata = joblib.load('models/final_optimized_metadata.pkl')
            print(f"✅ Optimized model loaded successfully!")
            print(f"🎯 Overall Accuracy: {self.metadata['overall_accuracy']:.2f}%")
            print(f"🌱 Environmental Accuracy: {self.metadata['environmental_accuracy']:.2f}%")
            print(f"♻️  Circularity Accuracy: {self.metadata['circularity_accuracy']:.2f}%")
        except Exception as e:
            print(f"❌ Error loading model: {e}")
            raise

    def predict_single(self, metal_type, supply_chain_complexity, production_volume, processing_method):
        """
        Predict environmental and circularity indicators for a single sample

        Returns:
        - Environmental predictions (Energy, Emissions, Water) - High accuracy (85%+)
        - Circularity predictions (Index, Content, Potential) - Optimized accuracy
        """
        # Prepare input data
        input_data = pd.DataFrame({
            'Metal_Type': [metal_type],
            'Supply_Chain_Complexity': [supply_chain_complexity],
            'Production_Volume_tons': [production_volume],
            'Processing_Method': [processing_method]
        })

        # Transform input
        X_transformed = self._prepare_features(input_data)

        # Environmental predictions
        env_pred = self.model_components['environmental_model'].predict(X_transformed)

        # Circularity predictions  
        best_circ_model = self.model_components['circularity_models'][
            self.model_components['circularity_best_model']
        ]

        if hasattr(best_circ_model, 'predict'):
            circ_pred = best_circ_model.predict(X_transformed)
        else:
            # MultiOutputRegressor
            circ_pred = best_circ_model.predict(X_transformed)

        # Combine predictions
        all_predictions = np.concatenate([env_pred[0], circ_pred[0]])

        # Format results
        results = {}
        all_targets = self.model_components['environmental_targets'] + self.model_components['circularity_targets']

        for i, target in enumerate(all_targets):
            results[target] = float(all_predictions[i])

        return results

    def _prepare_features(self, input_df):
        # Apply label encoding
        for column, encoder in self.model_components['label_encoders'].items():
            if column in input_df.columns:
                input_df[column] = encoder.transform(input_df[column])

        # Get numerical features
        numerical_features = ['Supply_Chain_Complexity', 'Production_Volume_tons']
        categorical_features = ['Metal_Type', 'Processing_Method']

        # Apply polynomial transformation
        poly_features = self.model_components['poly_transformer'].transform(
            input_df[numerical_features]
        )

        # Combine features
        X_transformed = np.concatenate([
            poly_features,
            input_df[categorical_features].values
        ], axis=1)

        return X_transformed

    def get_model_info(self):
        return self.metadata

# Example usage and testing
if __name__ == "__main__":
    try:
        predictor = OptimizedLCAPredictor()

        # Test prediction
        result = predictor.predict_single(
            metal_type=1,  # Encoded value
            supply_chain_complexity=3.5,
            production_volume=1000,
            processing_method=0  # Encoded value
        )

        print("\n🧪 Test Prediction Results:")
        for target, value in result.items():
            print(f"  {target}: {value:.4f}")

    except Exception as e:
        print(f"❌ Error in prediction: {e}")
