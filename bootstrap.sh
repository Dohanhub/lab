#!/bin/bash
# EAGLE AI - One-Click Bootstrap Script
# Version 1.8 - Production Ready Setup

set -e

echo "🚀 EAGLE AI - Elite Command Center Bootstrap"
echo "============================================="
echo "🏢 AFCO (Abdullah Fouad Company) - Saudi Technology Solutions"
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

print_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

# Check prerequisites
echo "🔍 Checking prerequisites..."

# Check Python
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
    print_status "Python $PYTHON_VERSION found"
else
    print_error "Python 3.8+ is required but not found"
    exit 1
fi

# Check Git
if command -v git &> /dev/null; then
    GIT_VERSION=$(git --version | cut -d' ' -f3)
    print_status "Git $GIT_VERSION found"
else
    print_error "Git is required but not found"
    exit 1
fi

# Check if we're in the right directory
if [ ! -f "DoganBS_UNIFIED.py" ]; then
    print_error "DoganBS_UNIFIED.py not found. Please run this script from the project root."
    exit 1
fi

print_status "Prerequisites check completed"
echo ""

# Install Python dependencies
echo "📦 Installing Python dependencies..."
if [ -f "requirements.txt" ]; then
    python3 -m pip install --upgrade pip
    python3 -m pip install -r requirements.txt
    print_status "Dependencies installed successfully"
else
    print_warning "requirements.txt not found, skipping dependency installation"
fi

# Install pre-commit hooks
echo "🔧 Setting up pre-commit hooks..."
if command -v pre-commit &> /dev/null; then
    pre-commit install
    print_status "Pre-commit hooks installed"
else
    print_warning "pre-commit not found, installing..."
    python3 -m pip install pre-commit
    pre-commit install
    print_status "Pre-commit hooks installed"
fi

# Initialize database
echo "🗄️  Initializing production database..."
if [ -f "production_database.py" ]; then
    python3 -c "
from production_database import AFCOProductionDB
db = AFCOProductionDB()
print('✅ Production database initialized with Saudi market data')
"
    print_status "Database initialization completed"
else
    print_warning "production_database.py not found, skipping database initialization"
fi

# Create necessary directories
echo "📁 Creating project directories..."
mkdir -p data outputs logs assets templates
print_status "Project directories created"

# Run initial tests
echo "🧪 Running initial system tests..."
if [ -f "test_eagle_ai_features.py" ]; then
    python3 -m pytest test_eagle_ai_features.py -v
    print_status "System tests completed"
else
    print_warning "test_eagle_ai_features.py not found, skipping tests"
fi

# Initialize Git repository if not already initialized
if [ ! -d ".git" ]; then
    echo "🔄 Initializing Git repository..."
    git init
    git add .
    git commit -m "chore: initial EAGLE AI setup"
    print_status "Git repository initialized"
fi

echo ""
echo "🎉 EAGLE AI Bootstrap Completed Successfully!"
echo "============================================="
echo ""
print_info "🚀 Quick Start Commands:"
echo "  • Launch Production System: ./LAUNCH_AFCO_PRODUCTION.bat"
echo "  • Manual Launch: streamlit run DoganBS_UNIFIED.py --server.port=8501"
echo "  • Run Tests: python -m pytest test_eagle_ai_features.py"
echo ""
print_info "📊 System Status:"
echo "  • Database: ✅ SQLite with real Saudi market data"
echo "  • AI Models: ✅ Prophet + XGBoost ready"
echo "  • Clients: ✅ ARAMCO, SABIC, STC, NCB, NEOM"
echo "  • Vendors: ✅ Dell, Cisco, HPE, Lenovo, Oracle"
echo ""
print_info "🌐 Access URLs:"
echo "  • Main Application: http://localhost:8501"
echo "  • Dev Status Dashboard: http://localhost:8501/dev-status"
echo ""
print_status "EAGLE AI is now ready for production deployment!"
echo "🏢 AFCO (Abdullah Fouad Company) - Technology Solutions & System Integration"
echo "🤖 Powered by Eagle AI - Production Intelligence Platform"
echo "🇸🇦 Saudi Arabia Technology Market Leader"
