CURRENTLY RUNS SERVER AND TEST CASES (Using mock values)

IF ON WINDOWS, FIRST DO THIS WHILE IN core_management (reformats endline):
    dos2unix entrypoint.sh

WHILE IN /osiris-function-library:
docker build -t osiris-function-library -f core_management/Dockerfile .
docker run -it osiris-function-library