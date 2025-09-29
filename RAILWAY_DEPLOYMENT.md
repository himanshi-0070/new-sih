# 🚄 Railway Deployment Guide for LCA-Mining

## 🎯 Quick Deploy to Railway

### Method 1: One-Click Deploy (Recommended)
[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/your-template-id)

### Method 2: Manual Deployment

#### Step 1: Prepare Your Repository
```bash
# Ensure all Railway config files are committed
git add railway.json nixpacks.toml .env.example
git commit -m "Add Railway deployment configuration"
git push origin main
```

#### Step 2: Deploy on Railway
1. Go to [Railway.app](https://railway.app/)
2. Sign in with GitHub
3. Click "New Project"
4. Select "Deploy from GitHub repo"
5. Choose `harirajharsh8795/LCA-Mining`
6. Railway will automatically detect and deploy

#### Step 3: Configure Environment Variables
In Railway dashboard → Variables tab, add:
```env
STREAMLIT_SERVER_HEADLESS=true
STREAMLIT_SERVER_ENABLE_CORS=false
STREAMLIT_BROWSER_GATHER_USAGE_STATS=false
PYTHONUNBUFFERED=1
```

## 🔧 Railway Configuration Files

### 📄 `railway.json`
- Railway service configuration
- Build and deploy commands
- Port and environment settings

### 📄 `nixpacks.toml`
- Nixpacks build configuration
- Python version and dependencies
- Build phases and commands

### 📄 `requirements.txt`
- Optimized for Railway platform
- Fixed versions for stability
- Railway-specific optimizations

## 🚀 Deployment Process

### Build Phase
1. **Environment Setup**: Python 3.11 + pip
2. **Dependency Installation**: requirements.txt
3. **Model Verification**: Check models directory
4. **Build Completion**: Ready for deployment

### Deploy Phase
1. **Service Start**: Streamlit server on $PORT
2. **Health Check**: Application readiness
3. **Public URL**: Railway generates domain
4. **SSL/HTTPS**: Automatic certificate

## 📊 Expected Performance

### 🎯 Railway Free Tier
- **CPU**: Shared vCPU
- **RAM**: 512MB (may need upgrade for large models)
- **Storage**: 1GB
- **Monthly Hours**: 500 hours free

### ⚡ Optimization Tips
1. **Model Size**: Consider model compression if >100MB
2. **Memory Usage**: Monitor RAM consumption
3. **Cold Starts**: ~10-30 seconds first load
4. **Concurrent Users**: Limited on free tier

## 🔍 Troubleshooting

### Common Issues & Solutions

#### Memory Errors
```bash
# Solution: Upgrade to Pro plan or optimize models
# Railway logs will show: "MemoryError" or "Killed"
```

#### Port Binding Issues
```bash
# Ensure using Railway's $PORT variable
streamlit run app/app.py --server.port $PORT
```

#### Model Loading Failures
```bash
# Check if Git LFS files downloaded
git lfs pull
```

#### Build Failures
```bash
# Check Railway logs for specific errors
# Usually dependency conflicts or Python version issues
```

## 📈 Monitoring & Logs

### Railway Dashboard Features
- **Real-time Logs**: View application logs
- **Metrics**: CPU, RAM, Network usage
- **Deployments**: History and rollback
- **Custom Domain**: Connect your domain

### Log Commands
```bash
# View latest logs
railway logs

# Follow logs in real-time
railway logs --follow
```

## 🔐 Security & Production

### Environment Variables
- Never commit sensitive data
- Use Railway's environment variables
- Enable HTTPS (automatic)

### Performance Monitoring
- Monitor memory usage
- Check response times
- Set up health checks

## 💰 Cost Optimization

### Free Tier Usage
- 500 hours/month free
- Auto-sleep after inactivity
- Shared resources

### Pro Tier Benefits ($5/month)
- Always-on services
- More CPU/RAM
- Priority support
- Custom domains

## 🎉 Post-Deployment

### Verify Deployment
1. **Access URL**: Railway provides public URL
2. **Test Functionality**: Generate predictions
3. **Check Visualizations**: Ensure charts load
4. **Monitor Performance**: Watch logs for errors

### Share Your App
```
Your LCA-Mining app is live at:
https://your-app-name.railway.app
```

## 📞 Support

### Railway Resources
- [Railway Docs](https://docs.railway.app/)
- [Railway Discord](https://discord.gg/railway)
- [Railway Status](https://status.railway.app/)

### Project Support
- GitHub Issues: [LCA-Mining Issues](https://github.com/harirajharsh8795/LCA-Mining/issues)
- Documentation: Project README.md

---

🚄 **Deploy your LCA-Mining project on Railway in minutes!** 🌱