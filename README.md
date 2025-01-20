# Spotify Music Recommendation System

A Python-based command-line application that generates personalized music recommendations using the Spotify API. This project was developed as part of CS110: Intro to Computer Programming with Python.

## Features

### Core Functionality
- **Genre-based Filtering**: Users can select from a curated list of music genres to seed recommendations
- **Artist Discovery**: Search and select artists to further refine music suggestions
- **Smart Recommendations**: Utilizes Spotify's recommendation algorithm to generate personalized track suggestions
- **Email Integration**: Share music recommendations via email using the SendGrid API

### User Interface
- Interactive command-line interface with error handling
- Clear display of selected genres and artists
- Formatted display of recommended tracks using pandas DataFrames
- Option to clear or update selection criteria at any time

## Technical Requirements

### Dependencies
```
sendgrid
pandas
ipython
certifi
```

### API Requirements
- Spotify API access (configured through authentication module)
- SendGrid API for email functionality

## Installation

1. Install required Python packages:
```bash
pip3 install sendgrid
pip3 install pandas
pip3 install ipython
pip3 install --upgrade certifi
```

2. Configure API Authentication:
- Navigate to the `apis/authentication.py` file
- Add your API credentials in the specified format

3. Verify installation by running the verification script:
```bash
cd tests
python3 run_verification.py
```

## Usage

1. Start the application:
```bash
python3 main.py
```

2. Follow the interactive prompts to:
   - Select music genres
   - Search and select artists
   - Generate recommendations
   - Email track suggestions to desired recipients

## Implementation Details

The application follows Spotify's recommendation system constraints:
- Requires at least one seed value (genre, artist, or track)
- Maximum of 5 combined seed values
- Supports various combinations of genres and artists for recommendation generation

## Project Structure

```
project/
├── apis/
│   ├── authentication.py
│   ├── sendgrid.py
│   └── spotify.py
├── tests/
│   └── run_verification.py
└── main.py
```

## Notes

- The application uses Spotify's official API to ensure up-to-date music recommendations
- Email functionality is implemented using SendGrid's API for reliable delivery
- Built with error handling to manage API rate limits and invalid user inputs

## Academic Context

This project was developed as part of CS110: Intro to Computer Programming with Python (Fall 2020). It demonstrates practical application of:
- API Integration
- Data Processing
- User Interface Design
- Error Handling
- External Service Integration
