# Copyright 2024 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Top-level package for Google Colaboratory."""

from google.colab import _installation_commands
from google.colab import _system_commands
from google.colab import auth
from google.colab import data_table
from google.colab import drive
from google.colab import files

__all__ = [
    'auth',
    'data_table',
    'drive',
    'files',
]


def load_ipython_extension(ipython):
  """Called by IPython upon loading the extension."""
  _system_commands.register_magics(ipython)
  _installation_commands.register_magics(ipython)
  print('Welcome to Google Colab!')
