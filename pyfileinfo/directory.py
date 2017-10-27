# -*- coding: utf-8 -*-

import os

from . import PyFileInfo, File


class Directory(File):
    def __init__(self, file_path):
        File.__init__(self, file_path)

    @staticmethod
    def is_valid(path):
        return os.path.isdir(path)

    def files_in(self, include_hidden_file=False, recursive=False):
        files = [PyFileInfo(os.path.join(self.path, filename))
                 for filename in os.listdir(self.path)]
        files.sort()

        for file in files:
            if file.is_hidden() and not include_hidden_file:
                continue

            yield file
            if recursive and file.is_directory():
                yield from file.files_in(include_hidden_file=include_hidden_file,
                                         recursive=recursive)

    @property
    def size(self):
        return sum([file.size for file in self.files_in(include_hidden_file=True)])
