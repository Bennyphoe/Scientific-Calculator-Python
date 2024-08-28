A Command line program written in Python, allowing users to choose an operation and input values to calculate a result!

`Learning Points`

1. Use a while True: Loop to keep the program running until a break is used
2. Import `math` module to get access to operations like Log, cos, sin, tan, sqrt, pow
3. inputs received are in string format, convert it to float using float(...) so can perform operations on it
4. convert result of operation back to string using str(...) so can concatenate with other strings
5. sin, cos and log takes in radians as value rather than degrees. degress = radians * 180 / pi, radians = degrees * pi / 180
6. Use pyinstaller to create a .exe file
7. pip install pyinstaller
8. pyinstaller --version
9. pyinstaller --onefile [app.py] -> creates a dist folder containing the executable file
