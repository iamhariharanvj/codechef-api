# CodeChef API

A simple Flask API that retrieves information about a Codechef user's solved practice problems in various categories.

## Table of Contents

- [Usage](#usage)
- [Local Deployment](#local-deployment)
- [API Endpoints](#api-endpoints)
- [Example](#example)
- [Contributing](#contributing)

## Usage

To use this API, make GET requests to the following endpoint:

```
https://codechef-api-peach.vercel.app/get/<username>
```

Replace `<username>` with the CodeChef username you want to fetch data for.

## Local Deployment

To run this Flask API locally, follow these steps:

1. Clone this repository:

   ```bash
   git clone https://github.com/iamhariharanvj/codechef-api.git
   ```

2. Change to the project directory:

   ```bash
   cd codechef-api
   ```

3. Create a virtual environment (Python 3.7+ recommended):

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:

   On Windows:

   ```bash
   venv\Scripts\activate
   ```

   On macOS and Linux:

   ```bash
   source venv/bin/activate
   ```

5. Install the required dependencies from `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

6. Start the Flask development server:

   ```bash
   python app.py
   ```

7. The API should now be running locally. Access it at:

   ```
   http://localhost:5000/get/<username>
   ```

   Replace `<username>` with the CodeChef username you want to fetch data for.

## API Endpoints

### Get CodeChef User Data

- **URL:** `/get/<username>`
- **Method:** GET
- **Parameters:**
  - `username` (string): The CodeChef username for which you want to fetch data.
- **Response:**

  - If the user exists, it returns a JSON object containing the user's coding scores and solved problems in different categories. Here's an example response:

    ```json
    {
      "problems": {
        "easy": {
          "count": 0,
          "problems": []
        },
        "hard": {
          "count": 0,
          "problems": []
        },
        "medium": {
          "count": 0,
          "problems": []
        },
        "school": {
          "count": 8,
          "problems": [
            {
              "contest_code": "-",
              "difficulty_rating": 200,
              "link": "https://www.codechef.com/problems/START01",
              "question": "Number Mirror",
              "submissions": 523328
            },
            // ... other problems in the "school" category
          ]
        }
      },
      "total_problems_solved": 10,
      "username": "hariharanvj"
    }
    
    ```

  - If the user doesn't exist or there is an error, it returns a JSON object with an error message.

## Contributing

If you want to contribute to this project, feel free to fork the repository and submit pull requests with your enhancements. I would highly appreciate it
