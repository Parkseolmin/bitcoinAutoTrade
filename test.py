import pyupbit

access = "OZ7NdR3EAyleF51hkt4xjxLVuHj0F3QsA5atFj2j"          # 본인 값으로 변경
secret = "ZxIGwwULMlxi9DwCOG9hHBpcTRvX5Ndd1IqqktHI"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-ETC"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회