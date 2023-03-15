# README

## Introduction

This program listens to the microphone input and generates a response based on the last spoken word that ends in "er" or "ers". If the phrase "stop listening" is spoken, the program will stop running. The response is generated using text-to-speech technology.

## Requirements

This program requires the following libraries to be installed:

-   vosk
-   pyaudio
-   pyttsx3

## Usage

To use this program, simply run the `start()` function. The program will start listening to the microphone input and generate a response when an appropriate word is detected.

## Configuration

This program uses the Vosk speech recognition model 'vosk-model-small-en-us-0.15' to recognize speech. If you wish to use a different model, modify the `model` variable in the `start()` function to the appropriate model path.

The `AUDIO_RATE` variable sets the sample rate of the audio input. If you are using a different sample rate, modify this variable to match your input.
