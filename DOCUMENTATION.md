# Documentation

## Usage

Create a python file example `console`

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os

dirname = os.path.dirname(os.path.realpath(__file__))

from phoopy.kernel import Kernel
from phoopy.console import Application # noqa
from cleo.inputs.argv_input import ArgvInput # noqa

_input = ArgvInput()

env = _input.get_parameter_option('--env', 'dev')
debug = not _input.has_option('--no-debug') and env != 'prod'

kernel = Kernel(env, debug)

application = Application(kernel)
application.run(_input)

```

Make it executable with `chmod`

```bash
$ chmod +x console
```

Then run

```bash
./console
```
