#c011934038@edu.teu.ac.jp
#L Ljt199627
from django.contrib import admin
from .models import N_word
from .models import V_word
from .models import Adj_word
from .models import Adv_word
from .models import In_word
from .models import Other_word
from .models import Memo_word

# Register your models here.
admin.site.register(N_word)
admin.site.register(V_word)
admin.site.register(Adj_word)
admin.site.register(Adv_word)
admin.site.register(In_word)
admin.site.register(Other_word)
