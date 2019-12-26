# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

import logging
import sys
import re
import unittest

from nikola.utils import LOGGER

from .test_rst_compiler import ReSTExtensionTestCase


class TestPublication(ReSTExtensionTestCase):

    extra_plugins_dirs = ["v7/publication_list/"]

    @staticmethod
    def setUpClass():
        LOGGER.notice('--- TESTS FOR publication_list')
        LOGGER.level = logging.WARNING

    @staticmethod
    def tearDownClass():
        sys.stdout.write('\n')
        LOGGER.level = logging.INFO
        LOGGER.notice('--- END OF TESTS FOR publication_list')

    def test_default(self):
        # the result should be
        expected = (
            '<div class="publication-list">'
            '<h3>2015</h3><ul>'
            '<li class="publication".*>.*One article in 2015.*'
            '<a href="https://example.com/papers/a2015.html">details</a>.*'
            '<a href="/pdf/a2015.pdf">full text</a>.*</li>'
            '<li class="publication".*>.*One conference in 2015.*'
            '<a href="https://example.com/papers/p2015.html">details</a>.*'
            '</li>'
            '</ul><h3>2010</h3><ul>'
            '<li class="publication".*>.*One Book in 2010.*'
            '<a href="https://example.com/papers/b2010.html">details</a>.*'
            '<a href="http://example.org/b2010.pdf">full text</a>.*</li>'
            '</ul></div>'
        )
        self.sample = ('.. publication_list:: tests/data/publication_list/test.bib '
                       'tests/data/publication_list/test1.bib'
                       '\n\t:highlight_author: Nikola Tesla')
        self.deps = 'tests/data/publication_list/test.bib'
        self.basic_test()
        assert re.search(
            expected.replace('\n', '').strip(),
            self.html.replace('\n', '').strip())


if __name__ == '__main__':
    unittest.main()
