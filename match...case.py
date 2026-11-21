def http_error(status):
    match status:
        case 400:
            return 'Bad request'
        case 404:
            return 'Not found'
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"


print(http_error(400))
print(http_error(404))
print(http_error(418))
print(http_error(500))


def check_permission(status):
    match status:
        case 200:
            return 'ok,请求成功'
        case 301 | 302:
            return 'redirect-重定向'
        case 401 | 403 | 404:
            return 'not allowed-无权限或未找到'
        case _:
            return 'unknow status-未知状态码'


for code in [200, 302, 403, 500, 418]:
    print(f'状态码{code}:{check_permission(code)}')
