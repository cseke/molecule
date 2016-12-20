#  Copyright (c) 2015-2016 Cisco Systems, Inc.
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to
#  deal in the Software without restriction, including without limitation the
#  rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
#  sell copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#  DEALINGS IN THE SOFTWARE.

import os

import pytest
import sh


@pytest.mark.parametrize(
    'with_scenario', ['docker'], indirect=['with_scenario'])
def test_command_converge(with_scenario):
    sh.molecule('converge')


@pytest.mark.parametrize(
    'with_scenario', ['docker'], indirect=['with_scenario'])
def test_command_create(with_scenario):
    sh.molecule('create')


@pytest.mark.parametrize(
    'with_scenario', ['docker'], indirect=['with_scenario'])
def test_command_destroy(with_scenario):
    sh.molecule('destroy')


def test_command_init_role(temp_dir):
    role_directory = os.path.join(temp_dir.strpath, 'test-init')
    sh.molecule('init', 'role', '--role-name', 'test-init')
    os.chdir(role_directory)

    sh.molecule('test')

# TODO(retr0h): Error if role dir already exists.
# TODO(retr0h): Error if scenario dir already exists.

@pytest.mark.parametrize(
    'with_scenario', ['docker'], indirect=['with_scenario'])
def test_command_lint(with_scenario):
    sh.molecule('lint')


@pytest.mark.parametrize(
    'with_scenario', ['docker'], indirect=['with_scenario'])
def test_command_test(with_scenario):
    sh.molecule('test')


@pytest.mark.parametrize(
    'with_scenario', ['docker'], indirect=['with_scenario'])
def test_command_verify(with_scenario):
    # TODO(retr0h): How should we best handle verify?
    # Should verify call converge first?
    sh.molecule('create')
    sh.molecule('converge')
    sh.molecule('verify')
