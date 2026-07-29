name: Build SinoBuilderAI APK

on:
  push:
    branches:
      - main
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Show repository structure
        run: |
          echo "Repository:"
          pwd
          ls -R
