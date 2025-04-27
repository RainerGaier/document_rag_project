# setup_and_run.ps1

# Move to script location
Set-Location -Path (Split-Path -Parent $MyInvocation.MyCommand.Definition)

# Check if venv exists
if (!(Test-Path -Path "venv")) {
    Write-Host "Creating virtual environment (venv)..."
    python -m venv venv
}

# Activate the virtual environment
Write-Host "Activating virtual environment..."
.\venv\Scripts\Activate.ps1

# Install required Python packages
Write-Host "Installing required packages..."
pip install --upgrade pip
pip install -r requirements.txt

# Set Streamlit safe file watcher setting
$env:STREAMLIT_WATCHER_TYPE="poll"
$env:KMP_DUPLICATE_LIB_OK="TRUE"

# Launch Streamlit app
Write-Host "Launching Streamlit app..."
streamlit run app.py

pause