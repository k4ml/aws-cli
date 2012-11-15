# Copyright 2012 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
#     http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
"""
AWSCLI
----
A Universal Command Line Environment for Amazon Web Services.
"""
import botocore.base
import os

__version__ = '0.1.0'

#
# Get our data path added to botocore's search path
#
p = os.path.split(__file__)[0]
p = os.path.split(p)[0]
botocore.base.add_data_path(os.path.join(p, 'awscli/data'))
if 'AWS_DATA_PATH' in os.environ:
    for path in os.environ['AWS_DATA_PATH'].split(':'):
        path = os.path.expandvars(path)
        path = os.path.expanduser(path)
        botocore.base.add_data_path(path)