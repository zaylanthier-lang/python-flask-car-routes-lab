# Flatiron Cars Flask App

This Flask application builds simple routes for a car company.

## Features

- `/` displays a welcome message.
- `/<model>` checks if a car model exists in the Flatiron Cars fleet.
- If the model exists, the app returns a fleet message.
- If the model does not exist, the app returns a catalog error message.

## Example Routes

```text
/ 
Welcome to Flatiron Cars!

/camry
Flatiron camry is in our fleet!

/pp
No models called pp exists in our catalog.