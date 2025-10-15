# Weather Station Dashboard

A real-time monitoring dashboard for tracking weather station data across India, built with Dash/Plotly, Pandas, and Python.

![Dashboard Preview](https://user-images.githubusercontent.com/63055601/188282067-f08e21ce-18cc-408e-888f-7b78c5925ddd.png)

## Overview

This dashboard provides real-time visualization of weather data from three types of monitoring systems:

- **SYNOP** (Manual stations) - Data received every 3 hours from manual weather observation stations
- **AWS** (Automated Weather Stations) - Automated stations sending data every hour
- **DRMS** (District Rainfall Monitoring System) - Weekly rainfall data across districts

The dashboard displays a rolling 7-day view, automatically updating as new data arrives and removing older data.

## Features

- **Real-time Updates**: Auto-refreshes every 20 seconds to display the latest data
- **Interactive Visualizations**: 
  - Bar charts showing station reporting trends over time
  - Pie charts displaying daily station reporting statistics
  - Color-coded indicators (Red: Low, Yellow: Medium, Green: Good)
- **Weekly Coverage**: Tracks 7 days of data with 7 individual pie charts for DRMS
- **Station Coverage**: Monitors 542+ weather stations across India

## Screenshots

### SYNOP Dashboard
![SYNOP View](https://user-images.githubusercontent.com/63055601/188281986-a881d290-3976-4bc0-9d30-49d15e60d51e.png)

### AWS Dashboard
![AWS View](https://user-images.githubusercontent.com/63055601/188281989-78e25809-03b5-4317-94a6-5efa3837b4b4.png)

## Installation

### Prerequisites

- Python 3.10 or higher
- pip package manager

### Required Libraries

```bash
pip install dash
pip install plotly
pip install pandas
pip install numpy
```

### Clone the Repository

```bash
git clone https://github.com/yourusername/Weather_Station_Dashboard.git
cd Weather_Station_Dashboard
```

## Configuration

Before running the dashboard, update the file paths in the following files to match your system:

### 1. `main.py`
```python
path = r'YOUR_PATH_TO_SYNOP_DATA'  # Line 110
path = r'YOUR_PATH_TO_AWS_DATA'     # Line 145
```

### 2. `DRMS.py`
```python
path = r"YOUR_PATH_TO_7_DAYS_DATA"
```

### 3. `aws.py` and `synop.py`
```python
path = r'YOUR_PATH_TO_DATA_FOLDER'
```

## Project Structure

```
Weather_Station_Dashboard/
│
├── main.py              # Main dashboard application
├── DRMS.py              # District Rainfall Monitoring System data processor
├── aws.py               # AWS data processor
├── synop.py             # SYNOP data processor
├── final_aws.csv        # AWS station master list (542 stations)
├── total_stations.txt   # Total number of DRMS stations
└── README.md            # This file
```

## Usage

1. Ensure your data files are in the correct locations (CSV files with semicolon separators)
2. Run the dashboard:

```bash
python main.py
```

3. Open your browser and navigate to:
```
http://127.0.0.1:8050/
```

4. The dashboard will automatically refresh every 20 seconds

## Data Format

### Input CSV Format
All CSV files should use semicolon (`;`) as the separator with the following structure:

```
#id;date;[other columns]
42027;15-10-2025 08:00:00;...
42034;15-10-2025 08:00:00;...
```

### Station ID Format
- SYNOP stations: IDs starting with '42' or '43'
- AWS stations: Listed in `final_aws.csv`

## Station Coverage

The dashboard monitors weather stations across all regions of India:
- Northern India (J&K, HP, Punjab, Haryana, Delhi, etc.)
- Eastern India (West Bengal, Odisha, Jharkhand, etc.)
- Western India (Gujarat, Rajasthan, Maharashtra, etc.)
- Southern India (Karnataka, Tamil Nadu, Kerala, etc.)
- North-Eastern India (Assam, Meghalaya, Manipur, etc.)

Full station list available in `final_aws.csv`

## Color Coding

### SYNOP Stations
- 🟢 **Green (250+)**: Excellent coverage
- 🟡 **Yellow (150-250)**: Good coverage
- 🔴 **Red (0-150)**: Low coverage

### AWS Stations
- 🟢 **Green (80+)**: Excellent coverage
- 🟡 **Yellow (60-80)**: Good coverage
- 🔴 **Red (0-60)**: Low coverage

### DRMS Pie Charts
- 🟢 **Green**: Stations reporting
- 🔴 **Red**: Missing stations

## Technologies Used

- **Dash**: Web application framework
- **Plotly**: Interactive visualizations
- **Pandas**: Data manipulation and analysis
- **Python 3.10**: Core programming language

## Troubleshooting

### Common Issues

1. **"FileNotFoundError"**: Update file paths in configuration section
2. **Empty graphs**: Ensure CSV files exist and contain data
3. **Encoding errors**: CSV files should use 'latin-1' encoding
4. **Dashboard not loading**: Check if port 8050 is available

## Future Enhancements

- [ ] Add database integration for historical data
- [ ] Include weather parameter analysis (temperature, rainfall, etc.)
- [ ] Add email alerts for low station coverage
- [ ] Export functionality for reports
- [ ] Mobile-responsive design improvements

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

## Contact

For questions or suggestions, please open an issue on GitHub.

---

**Note**: This dashboard is designed for monitoring weather station network health and data availability. It does not display actual weather parameters but focuses on station reporting statistics.
