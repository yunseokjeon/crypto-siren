from django.db import models

# Create your models here.

class CryptoTicker(models.Model):
    id = models.BigAutoField(primary_key=True)
    exchange = models.CharField(max_length=20)
    register_date = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=50)
    opening_price = models.DecimalField(decimal_places=15, max_digits=35)
    high_price = models.DecimalField(decimal_places=15, max_digits=35)
    low_price = models.DecimalField(decimal_places=15, max_digits=35)
    trade_price = models.DecimalField(decimal_places=15, max_digits=35)
    prev_closing_price = models.DecimalField(decimal_places=15, max_digits=35)
    acc_trade_price = models.DecimalField(decimal_places=15, max_digits=35)
    change = models.CharField(max_length=10)
    change_price = models.DecimalField(decimal_places=15, max_digits=35)
    signed_change_price = models.DecimalField(decimal_places=15, max_digits=35)
    change_rate = models.DecimalField(decimal_places=15, max_digits=35)
    signed_change_rate = models.DecimalField(decimal_places=15, max_digits=35)
    ask_bid = models.CharField(max_length=10)
    trade_volume = models.DecimalField(decimal_places=15, max_digits=35)
    acc_trade_volume = models.DecimalField(decimal_places=15, max_digits=35)
    trade_date = models.DateTimeField()
    trade_timestamp = models.BigIntegerField()
    acc_ask_volume = models.DecimalField(decimal_places=15, max_digits=35)
    acc_bid_volume = models.DecimalField(decimal_places=15, max_digits=35)
    server_timestamp = models.BigIntegerField()
    acc_trade_price_24h = models.DecimalField(decimal_places=15, max_digits=35)
    acc_trade_volume_24h = models.DecimalField(decimal_places=15, max_digits=35)

class CryptoTrade(models.Model):
    id = models.BigAutoField(primary_key=True)
    exchange  = models.CharField(max_length=20)
    register_date = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=50)
    server_timestamp = models.BigIntegerField()
    trade_date = models.DateTimeField()
    trade_timestamp = models.BigIntegerField()
    trade_price = models.DecimalField(decimal_places=15, max_digits=35)
    trade_volume = models.DecimalField(decimal_places=15, max_digits=35)
    ask_bid = models.CharField(max_length=10)
    change = models.CharField(max_length=10)
    change_price = models.DecimalField(decimal_places=15, max_digits=35)
    sequential_id = models.BigIntegerField()

class CryptoOrderbookMain(models.Model):
    id = models.BigAutoField(primary_key=True)
    exchange = models.CharField(max_length=20)
    register_date = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=50)
    server_timestamp = models.BigIntegerField()
    total_ask_size = models.DecimalField(decimal_places=15, max_digits=35)
    total_bid_size = models.DecimalField(decimal_places=15, max_digits=35)

class CryptoOrderbookSub(models.Model):
    id = models.BigAutoField(primary_key=True)
    main_key = models.BigIntegerField()
    register_date = models.DateTimeField(auto_now_add=True)
    ask_price = models.DecimalField(decimal_places=15, max_digits=35)
    bid_price = models.DecimalField(decimal_places=15, max_digits=35)
    ask_size = models.DecimalField(decimal_places=15, max_digits=35)
    bid_size = models.DecimalField(decimal_places=15, max_digits=35)



