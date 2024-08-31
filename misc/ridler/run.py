import types

code = """def test(num_list):
  min = 1000
  max = -1000
  for num in num_list:
    if min > num: min = num
    if max < num: max = num
  return (min, max)"""
c = compile(code, '<string>', 'exec')
answer = c.co_consts[0].co_code

answer = ','.join(str(k) for k in answer)

print(answer)

answer_b = bytes([int(b) for b in answer.strip().split(",")])

co_code_start = b"d\x01}\x01d\x02}\x02"
co_code_end = b"|\x01|\x02f\x02S\x00"
co_code = bytearray(co_code_start)
co_code.extend(answer_b)
co_code.extend(co_code_end)

_answer_func = types.FunctionType(
    types.CodeType(
        1,
        0,
        0,
        4,
        3,
        3,
        bytes(co_code),
        (None, 1000, -1000),
        (),
        ("num_list", "min", "max", "num"),
        __file__,
        "_answer_func",
        "_answer_func",
        1,
        b"",
        b"",
        (),
        (),
    ), {}
)

print(_answer_func([1,2,3,4,5]))
