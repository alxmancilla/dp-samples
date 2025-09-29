# dp-samples

This repository contains small sample implementations of common design patterns and other JavaScript and Python examples.

These examples were implemented approximately 10 years ago and are intended as simple, educational snippets rather than production-ready code. Expect older language idioms and minimal dependency management.

Top-level folders and notable files
- `javascript/` — JavaScript pattern examples (Factory, Singleton, Adapter, Builder, Composite, Command, etc.). Open the files in a browser or run them with Node.js where appropriate.
- `python/` — Python examples of design patterns and small utilities (Factory, Observer, Decorator, MVC, Strategy, etc.). Many scripts are runnable with Python 3.x but may use older conventions.
- `mysql/` — small MySQL test scripts.
- `MVCTemplate.py`, `MVCTemplateFilled.py` — example MVC templates in Python.

Quick start

- To run Python examples (recommended Python 3):

  1. Create a virtual environment and activate it.
  2. Run an example directly, e.g. `python3 python/sample1.py` or `python3 python/MVC.py`.

- To run JavaScript examples:

  - Install Node.js (v14+ recommended for older examples)
  - Run a file with `node javascript/SingletonPattern.js` (or open in a browser if the example uses browser APIs).

Notes and caveats

- These are simple, standalone examples meant for learning. They may not follow modern best practices or include tests.
- Use caution if you intend to reuse code — update to modern language features and add tests before production use.

Contributions

Feel free to open issues or pull requests to modernize examples, add tests, or include additional patterns.

License

This repository is provided as-is for educational purposes.
