__all__ = (
    'seconds_to_str',
)
from datetime import datetime

def seconds_to_str(seconds: int) -> str:
   m, s = divmod(seconds, 60)
   h, m = divmod(m, 60)
   d, h = divmod(h, 24)
   if seconds < 60:
       return f'{s:02d}s'
   elif seconds < 3600:
       return f'{m:02d}m{s:02d}s'
   elif seconds < 86400:
       return f'{h:02d}h{m:02d}m{s:02d}s'
   else:
       return f'{d:02d}d{h:02d}h{m:02d}m{s:02d}s'
