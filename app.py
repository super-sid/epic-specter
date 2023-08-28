#!/usr/bin/env python

# Main application entry point
if __name__ == "__main__":
    # Initialize database connection
    from database import Database
    db = Database()

    # Start the application loop
    app_loop()