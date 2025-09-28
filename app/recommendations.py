import numpy as np

def get_environmental_recommendations(predictions):
    """Generate environmental improvement recommendations based on predictions"""
    recommendations = []
    
    # Extract environmental values
    energy = predictions.get('Energy_Use_MJ_per_kg', 0)
    emissions = predictions.get('Emission_kgCO2_per_kg', 0)
    water = predictions.get('Water_Use_l_per_kg', 0)
    
    # Energy recommendations
    if energy > 150:
        recommendations.append("🔥 **High Energy Usage**: Consider switching to renewable energy sources or optimizing process efficiency")
        recommendations.append("⚡ Implement energy recovery systems to capture and reuse waste heat")
    elif energy > 100:
        recommendations.append("💡 **Moderate Energy Usage**: Look into energy-efficient equipment upgrades")
    else:
        recommendations.append("✅ **Good Energy Performance**: Current energy usage is within acceptable limits")
    
    # Emissions recommendations
    if emissions > 15:
        recommendations.append("🌫️ **High CO₂ Emissions**: Urgent need to implement carbon capture technologies")
        recommendations.append("🌱 Consider switching to low-carbon production methods or renewable energy")
    elif emissions > 10:
        recommendations.append("📉 **Moderate Emissions**: Implement emission reduction strategies like process optimization")
    else:
        recommendations.append("🌿 **Low Emissions**: Excellent carbon performance, maintain current practices")
    
    # Water usage recommendations
    if water > 80:
        recommendations.append("💧 **High Water Usage**: Implement water recycling and closed-loop systems")
        recommendations.append("🔄 Consider dry processing methods where technically feasible")
    elif water > 50:
        recommendations.append("💦 **Moderate Water Usage**: Optimize water efficiency in production processes")
    else:
        recommendations.append("💙 **Efficient Water Use**: Good water management practices in place")
    
    # General environmental recommendations
    recommendations.append("🏭 **Process Optimization**: Regular maintenance and process tuning can reduce all environmental impacts")
    recommendations.append("📊 **Monitoring**: Implement real-time monitoring systems for continuous improvement")
    
    return recommendations

def get_circularity_recommendations(predictions):
    """Generate circularity improvement recommendations based on predictions"""
    recommendations = []
    
    # Extract circularity values
    circularity_index = predictions.get('Circularity_Index', 0)
    recycled_content = predictions.get('Recycled_Content_pct', 0)
    reuse_potential = predictions.get('Reuse_Potential_score', 0)
    
    # Circularity Index recommendations
    if circularity_index < 0.3:
        recommendations.append("♻️ **Low Circularity**: Major improvements needed in circular design principles")
        recommendations.append("🔄 Focus on design for disassembly and material recovery")
        recommendations.append("🎯 Set targets for increasing material circularity by 25% within 2 years")
    elif circularity_index < 0.6:
        recommendations.append("📈 **Moderate Circularity**: Good foundation, aim for further improvements")
        recommendations.append("🔧 Enhance product durability and repairability features")
    else:
        recommendations.append("🏆 **Excellent Circularity**: Leading circular economy practices")
    
    # Recycled Content recommendations
    if recycled_content < 20:
        recommendations.append("📦 **Low Recycled Content**: Increase use of secondary raw materials")
        recommendations.append("🤝 Establish partnerships with recycling companies for material supply")
        recommendations.append("🎯 Target minimum 30% recycled content in production")
    elif recycled_content < 50:
        recommendations.append("♻️ **Moderate Recycling**: Continue increasing recycled material usage")
        recommendations.append("🔍 Identify opportunities to substitute virgin materials with recycled alternatives")
    else:
        recommendations.append("🌟 **High Recycled Content**: Excellent use of secondary materials")
    
    # Reuse Potential recommendations
    if reuse_potential < 0.3:
        recommendations.append("🔧 **Low Reuse Potential**: Design products for multiple life cycles")
        recommendations.append("📝 Develop take-back programs for end-of-life products")
        recommendations.append("🏗️ Create modular designs that enable component reuse")
    elif reuse_potential < 0.6:
        recommendations.append("🔄 **Moderate Reuse**: Enhance product design for better reusability")
        recommendations.append("📋 Implement product-as-a-service models")
    else:
        recommendations.append("🎉 **High Reuse Potential**: Excellent design for reusability")
    
    # Specific improvement strategies
    recommendations.append("🏭 **Supply Chain**: Collaborate with suppliers to improve material traceability")
    recommendations.append("📱 **Digital Tools**: Implement digital passports for material tracking")
    recommendations.append("🎓 **Training**: Educate staff on circular economy principles and practices")
    
    return recommendations

def get_process_specific_recommendations(metal_type, process_type):
    """Generate recommendations specific to metal type and process"""
    recommendations = []
    
    # Metal-specific recommendations
    metal_recommendations = {
        'Aluminum': [
            "⚡ Aluminum recycling uses 95% less energy than primary production",
            "🔋 Consider using hydroelectric power for smelting operations",
            "🏭 Implement advanced sorting technologies for scrap aluminum"
        ],
        'Steel': [
            "🔥 Electric arc furnaces are more efficient for steel recycling",
            "💨 Implement blast furnace gas recovery systems",
            "🧲 Use magnetic separation for improved scrap quality"
        ],
        'Copper': [
            "⚡ Copper has excellent recycling properties with minimal quality loss",
            "🔧 Focus on improving scrap collection and sorting systems",
            "🏭 Consider hydrometallurgical processes for complex ores"
        ]
    }
    
    # Process-specific recommendations
    process_recommendations = {
        'Primary Production': [
            "🌱 Transition to renewable energy sources",
            "⚙️ Optimize extraction and processing efficiency",
            "💧 Implement water recycling systems"
        ],
        'Secondary Production (Recycling)': [
            "🔄 Excellent choice for environmental sustainability",
            "📊 Focus on improving sorting and contamination removal",
            "🎯 Maintain high recycling rates through quality control"
        ],
        'Hybrid Process': [
            "⚖️ Balance virgin and recycled materials for optimal performance",
            "🔬 Monitor material quality throughout the process",
            "📈 Gradually increase recycled content percentage"
        ]
    }
    
    # Add metal-specific recommendations
    if metal_type in metal_recommendations:
        recommendations.extend(metal_recommendations[metal_type])
    
    # Add process-specific recommendations
    if process_type in process_recommendations:
        recommendations.extend(process_recommendations[process_type])
    
    return recommendations

def get_cost_optimization_recommendations(cost_per_kg, predictions):
    """Generate cost optimization recommendations"""
    recommendations = []
    
    energy = predictions.get('Energy_Use_MJ_per_kg', 0)
    recycled_content = predictions.get('Recycled_Content_pct', 0)
    
    if cost_per_kg > 10:
        recommendations.append("💰 **High Production Cost**: Focus on cost reduction strategies")
        if energy > 100:
            recommendations.append("⚡ Energy costs are likely significant - invest in efficiency improvements")
        if recycled_content < 30:
            recommendations.append("♻️ Increase recycled content to reduce raw material costs")
    elif cost_per_kg > 5:
        recommendations.append("💵 **Moderate Cost**: Look for incremental cost improvements")
        recommendations.append("📊 Benchmark against industry standards for cost optimization")
    else:
        recommendations.append("✅ **Cost Efficient**: Maintain current cost-effective practices")
    
    # General cost optimization strategies
    recommendations.extend([
        "🤖 **Automation**: Consider automation for labor-intensive processes",
        "📈 **Scale**: Evaluate opportunities for economies of scale",
        "🔗 **Supply Chain**: Optimize supply chain logistics and inventory management"
    ])
    
    return recommendations

def get_regulatory_compliance_recommendations():
    """Generate recommendations for regulatory compliance"""
    recommendations = [
        "📋 **Environmental Regulations**: Ensure compliance with local emission standards",
        "♻️ **Waste Regulations**: Follow proper waste management and reporting requirements",
        "🏭 **Industrial Standards**: Maintain compliance with industry-specific regulations",
        "📊 **Reporting**: Implement systematic environmental reporting and documentation",
        "🔍 **Auditing**: Regular third-party environmental audits for compliance verification",
        "🎯 **Targets**: Set science-based targets aligned with Paris Agreement goals",
        "💼 **Corporate Responsibility**: Develop comprehensive sustainability reporting",
        "🌍 **International Standards**: Consider ISO 14001 environmental management certification"
    ]
    
    return recommendations

def get_technology_recommendations(predictions):
    """Generate technology upgrade recommendations based on performance"""
    recommendations = []
    
    energy = predictions.get('Energy_Use_MJ_per_kg', 0)
    emissions = predictions.get('Emission_kgCO2_per_kg', 0)
    circularity_index = predictions.get('Circularity_Index', 0)
    
    # Energy-based technology recommendations
    if energy > 120:
        recommendations.extend([
            "🔋 **Energy Storage**: Implement battery systems for load balancing",
            "🌡️ **Heat Recovery**: Install waste heat recovery systems",
            "⚡ **Smart Grid**: Connect to smart grid for optimal energy management"
        ])
    
    # Emissions-based technology recommendations
    if emissions > 12:
        recommendations.extend([
            "🌿 **Carbon Capture**: Consider CO₂ capture and utilization technologies",
            "🔬 **Process Innovation**: Invest in low-carbon process technologies",
            "📡 **Monitoring**: Deploy continuous emissions monitoring systems"
        ])
    
    # Circularity-based technology recommendations
    if circularity_index < 0.4:
        recommendations.extend([
            "🤖 **AI Sorting**: Implement AI-powered material sorting systems",
            "📱 **Blockchain**: Use blockchain for material traceability",
            "🔧 **IoT Sensors**: Deploy IoT for real-time process monitoring"
        ])
    
    # General technology recommendations
    recommendations.extend([
        "🏭 **Industry 4.0**: Adopt digital manufacturing technologies",
        "📊 **Analytics**: Implement predictive analytics for process optimization",
        "🌐 **Digital Twin**: Develop digital twin models for process simulation"
    ])
    
    return recommendations