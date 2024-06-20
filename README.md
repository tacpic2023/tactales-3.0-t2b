# tactales-3.0-t2b
# Text-To-Braille module for Tac-Tales 3.0 Implementation

## Build a new Docker Image

### Prerequisites: Ubuntu/Linux; Visual Studio Code with WSL, Docker, and Python extensions

#### Using Visual Studio Code:

With all extensions set up, click the lower left green >< button to "Open a Remote Window" to connect to WSL/Ubuntu in Windows

#### Using Ubuntu Terminal:

Clone the repository

```
  git clone https://github.com/tacpic2023/tactales-3.0-backend.git
```

Relocate work directory

```
  cd tactales-3.0-backend
```

Clone the liblouis repository

```
  git clone https://github.com/liblouis/liblouis.git
```

Install necessary sudo package

```
  sudo apt-get install autoconf automake libtool build-essential libssl-dev python3-dev
  sudo apt-get update
```

Set up liblouis

```
  cd liblouis
  ./autogen.sh && ./configure --enable-ucs4 && make && make install && ldconfig
```

Build the image. With Google Cloud Run naming conventions

```
  cd ..
  docker build -t gcr.io/poised-shuttle-417103/tacpic-backend .
```