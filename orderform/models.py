from django.db import models
# Create your models here.

class order(models.Model):
    cName = models.CharField(max_length=20, null=False, verbose_name="訂購者")
    cSpot = models.CharField(max_length=20, default="自取",null=False, verbose_name="取貨地點")
    cPhone = models.CharField(max_length=10, null=False, verbose_name="聯絡電話")
    cDate = models.DateField(null=False, verbose_name="取貨日期")

    c1T100 = models.IntegerField(verbose_name="鮮奶吐司")
    c1T100_slice = models.CharField(max_length=10, default="不切", null=False, verbose_name="鮮奶吐司-切片")
    c1T100_thickless = models.CharField(max_length=10, default="", verbose_name="鮮奶吐司-厚度")

    c1T120 = models.IntegerField(verbose_name="葡萄乾吐司")
    c1T120_slice = models.CharField(max_length=10, default="不切", null=False, verbose_name="葡萄乾吐司-切片")
    c1T120_thickless = models.CharField(max_length=10, default="", verbose_name="葡萄乾吐司-厚度")

    c1T130 = models.IntegerField(verbose_name="蔓越莓吐司")
    c1T130_slice = models.CharField(max_length=10, default="不切", null=False, verbose_name="蔓越莓吐司-切片")
    c1T130_thickless = models.CharField(max_length=10, default="", verbose_name="蔓越莓吐司-厚度")

    c1T140 = models.IntegerField(verbose_name="核桃吐司")
    c1T140_slice = models.CharField(max_length=10, default="不切", null=False, verbose_name="核桃吐司-切片")
    c1T140_thickless = models.CharField(max_length=10, default="", verbose_name="核桃吐司-厚度")

    c2M50 = models.IntegerField(verbose_name="酵母鬆餅")
    c2M50_slice = models.CharField(max_length=10, default="不切", verbose_name="酵母鬆餅-切片")
