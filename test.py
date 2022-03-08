import pyupbit

access = "M7ZmYWJYgBUqYIWFWSOs5ch9XIreIcuMK62kY0Ax"          # 본인 값으로 변경
secret = "SGxPf2xbOURTw4v0LHt6kDHRuKSz57BraNYdYlHV"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-BTC"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회