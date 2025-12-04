# 🎿 Slovakia Ski Touring Trails Explorer

> Discover the best ski touring routes across the majestic Tatras mountains

An interactive web app showcasing 10 premier ski touring trails in Slovakia, featuring real elevation profiles, detailed
trail stats, and stunning mountain imagery.

## ✨ Features

- **📊 Interactive Trail Database** - Browse 10 authentic ski touring routes from High Tatras, Low Tatras, and Western
  Tatras
- **📈 Dynamic Elevation Profiles** - Beautiful, interactive altitude charts showing ascent and descent with peak markers
- **🏔️ Detailed Trail Stats** - View length, duration, elevation gain, difficulty level, and mountain range for each
  trail
- **🌓 Dark/Light Mode** - Toggle between themes for comfortable viewing
- **📱 Responsive Design** - Works seamlessly on desktop and mobile devices

## 🚀 Quick Start

### Prerequisites

- Python 3.13+
- [uv](https://github.com/astral-sh/uv) package manager

### Installation

```bash
# Install dependencies
uv sync

# Run the app
streamlit run main.py
```

The app will open in your browser at `http://localhost:8501`

## 🛠️ Tech Stack

- **Streamlit** - Web framework
- **ECharts** - Interactive visualizations
- **Pandas** - Data handling
- **NumPy & SciPy** - Altitude profile generation
- **Python 3.13** - Core language

## 📚 Data Sources

Trail data contain dummy values

## 📁 Project Structure

```
lab-streamlit/
├── main.py                 # Main Streamlit application
├── src/
│   ├── trail_data.py       # Trail database with dummy data
│   ├── ...                 # Components 
├── assets/
│   └── sk-topography.png  # Slovakia topography image
├── pyproject.toml         # Project dependencies
└── README.md              # This file
```

## 📄 License

This project is open source and available under the MIT License.

---

*Made with ❤️ for mountain enthusiasts*
