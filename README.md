# G-App Suite Calculator

## Overview
The G-App Suite Calculator is a versatile and user-friendly calculator application designed for the G-App Suite ecosystem. This repository contains the source code and resources for the Calculator, suitable for performing basic and advanced mathematical operations.

## Features
- **Basic Arithmetic**: Supports addition, subtraction, multiplication, and division.
- **Cross-Platform**: Compatible with Windows, macOS, and Linux.

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/gunungpw/gapp-calculator.git
   ```
2. **Navigate to the Project Directory**:
   ```bash
   cd gapp-calculator
   ```
3. **Install UV**:
   Install `uv` using the official installation method. Follow the instructions for your operating system from the [official UV documentation](https://docs.astral.sh/uv/getting-started/installation/). For example, on Unix-based systems (Linux/macOS):
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```
   For Windows, use PowerShell:
   ```bash
   powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```
4. **Install Dependencies**:
   Use `uv` to install dependencies defined in `pyproject.toml`. This will create a virtual environment and install the required packages.
   ```bash
   uv sync
   ```
5. **Run the Application**:
   Activate the virtual environment and run the application:
   ```bash
   uv run src/main.py
   ```

## Usage
- Launch the application to access the calculator interface.
- Perform calculations using the on-screen keypad or keyboard input.

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a Pull Request.

Please ensure your code adheres to the project's coding standards and includes appropriate tests.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact
For questions or support, please open an issue on the [GitHub Issues page](https://github.com/gunungpw/gapp-calculator/issues) or contact the maintainer at gunungpambudiw@gmail.com.

---

&copy; 2025 Gunung Pambudi Wibisono. All rights reserved.
