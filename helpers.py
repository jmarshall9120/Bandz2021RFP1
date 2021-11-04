class DisplayHelper:

  def __init__(self, gbls):
    self.gbls = gbls
    return

  def format(self, name):
    return f"{name} = {self.gbls.get(name)}"

  def __call__(self, *args):
    return '\n'.join(self.format(s) for s in args).rstrip('\n')