# Project Title

A brief description of your project.

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the backend directory:
   ```
   cd backend
   ```
3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Environment Variables

Create a `.env` file in the backend directory and add the following variables:

```
DATABASE_URL=<your-database-url>
SECRET_KEY=<your-secret-key>
```

## Usage

To run the application, execute the following command:

```
uvicorn src.main:app --reload
```

Visit `http://127.0.0.1:8000` in your browser to access the API.

## API Endpoints

- **GET /products**: Retrieve a list of products.
- **GET /featured**: Retrieve featured products.
- **POST /search**: Search for products by title.
- **POST /purchase**: Purchase a product.
- **GET /user**: Retrieve user information.
- **POST /chat/send**: Send a chat message.
- **GET /chat/{user_id}**: Retrieve chat messages for a user.

## Contributing

1. Fork the repository.
2. Create a new branch:
   ```
   git checkout -b feature/YourFeature
   ```
3. Make your changes and commit them:
   ```
   git commit -m "Add your message"
   ```
4. Push to the branch:
   ```
   git push origin feature/YourFeature
   ```
5. Create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.