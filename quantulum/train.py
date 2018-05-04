#!/usr/bin/env python

'''
Retrain the quantulum classifier that disambiguates possible matches based on
wikipedia text.
'''

from . import classifier


def main():
    classifier.train_classifier()


if __name__ == '__main__':
    main()
