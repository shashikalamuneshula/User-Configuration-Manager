# User Configuration Manager

A lightweight, robust Python application designed to manage, update, and persist user preferences and system settings. Built as part of the **freeCodeCamp Full-Stack Developer / Python Certification** curriculum.

The project demonstrates advanced use of Python dictionaries, string normalization, tuple unpacking, data validation, and automated CRUD operations for application states.

## 🚀 Features

- **Add New Settings**: Dynamically insert new configuration pairs with automatic duplicate checking and name collision avoidance.
- **Update Settings**: Safely update values for existing configurations while enforcing state validation.
- **Delete Settings**: Seamlessly purge configurations from active tracking by their specific keys.
- **View Configuration Matrix**: Output cleanly structured representations of all current key-value preferences.
- **String Normalization**: Built-in case-insensitive validation for safe parameter processing.

## 🛠️ Tech Stack & Concepts

- **Language:** Python 3.x
- **Data Structures:** Dictionaries, Tuples, Lists
- **Concepts Applied:** Control flow structures, error checking, text manipulation, and defensive programming.

## 📋 Project Specifications & Methods Implemented

The manager exposes core functional APIs mapped to user configuration management tasks:

### 1. `add_setting(settings, values)`
Accepts the master settings dictionary and a tuple containing `(key, value)`. Checks if the lowercased key exists; if unique, it populates it and returns a success verification string.

### 2. `update_setting(settings, values)`
Validates existence of target parameters. Modifies existing active state and rejects manipulation of unregistered variables.

### 3. `delete_setting(settings, key)`
Locates the specific configuration attribute using its distinct key map and drops it completely from the session lifecycle using Python dictionary operations.

### 4. `view_settings(settings)`
Evaluates whether any preferences are currently registered. Formats active settings into readable summaries or surfaces fallback notices when empty.

## ⚙️ Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   ```

2. **Navigate into the directory:**
   ```bash
   cd user-configuration-manager
   ```

3. **Run or test the script:**
   ```bash
   python main.py
   ```

## 🤝 Acknowledgments

- Built according to the user stories and labs set by [freeCodeCamp](https://www.freecodecamp.org).
