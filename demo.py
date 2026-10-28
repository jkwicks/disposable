"""Disposable live-delivery demonstration."""


def normalize(name):
    return name.strip()


def label(name):
    return f"Hello, {normalize(name)}!"


def labels(names):
    return [label(name) for name in names]
