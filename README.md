
# Quote Generator

This is a simple project built with **Django** that randomly generates and displays motivational quotes. It features a modern, minimalistic design with neon animations that enhance the UI and provide a visually appealing experience.

## Features

- **Random Quote Generator**: Every time the page is refreshed, a new motivational quote is displayed.
- **Neon Design**: Custom CSS is used to create a neon border effect for the quotes and buttons, with a smooth, continuous animation.
- **Minimalistic Interface**: The interface is designed to be clean and simple, focusing on the quotes without unnecessary distractions.

## Tech Stack

- **Backend**: Django 5.0
- **Frontend**: HTML, CSS (Custom Neon Animations), Bootstrap
- **Randomization**: Python's `random` module to generate quotes

## How It Works

When the page loads, a random quote is selected from a pre-defined list in `views.py`. The selected quote is then passed to the frontend and displayed inside a bordered container that has a neon-like glow thanks to CSS animations.

The neon effect is achieved using the following CSS properties:

```css
@keyframes gradient-border {
    0% {
        border-image: linear-gradient(45deg, #ff00ff, #00ffff) 1;
    }
    50% {
        border-image: linear-gradient(45deg, #00ff00, #ff0000) 1;
    }
    100% {
        border-image: linear-gradient(45deg, #ff00ff, #00ffff) 1;
    }
}

#quote {
    border-width: 5px;
    border-style: solid;
    border-image: linear-gradient(45deg, #ff00ff, #00ffff) 1;
    animation: gradient-border 6s infinite;
}
```

## Setup Instructions

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/quote-generator.git
    cd quote-generator
    ```

2. **Install dependencies**:
    Ensure you have `pipenv` or `virtualenv` set up, then run:
    ```bash
    pip install django
    ```

3. **Run the Django server**:
    ```bash
    python manage.py runserver
    ```

4. **View the project**:
    Open your web browser and navigate to `http://127.0.0.1:8000/` to see the random quote generator in action.

## Customization

To customize the quotes, simply edit the `citas` list in the `views.py` file:
```python
citas = [
    "The only way to do great work is to love what you do. – Steve Jobs",
    "Life is what happens when you're busy making other plans. – John Lennon",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. – Winston Churchill",
    # Add more quotes here
]
```

## Project Structure

```plaintext
quotegenerator/
├── manage.py
├── quotegenerator/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── quotegeneratorapp/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── static/
│   ├── css/
│   │   ├── bootstrap.min.css
│   │   └── neon.css
│   └── js/
│       ├── bootstrap.min.js
│       └── bootstrap.min.js.map
└── templates/
    └── index.html
```

## License

This project is licensed under the MIT License. Feel free to fork it, improve it, and use it in your own projects!

---

**Happy Coding!**
