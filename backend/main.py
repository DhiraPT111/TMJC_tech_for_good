"""Runs the backend."""
import sys

import classifier
import object_detector


def main(argv):
  image = b'asdf'
  screen = object_detector.DetectScreen(image)
  what_is_on_the_screen = classifier.ClassifyScreen(screen)
  print('got screen type', what_is_on_the_screen)


if __name__ == '__main__':
  main(sys.argv)
