import os
import socket


def run_server(port=53210):
    serv_sock = create_serv_sock(port) # type: ignore
    active_children = set()
    cid = 0
    while True:
        client_sock = accept_client_conn(serv_sock, cid) # type: ignore
        child_pid = serve_client(client_sock, cid)
        active_children.add(child_pid)
        reap_children(active_children)
        cid += 1

def serve_client(client_sock, cid):
        child_pid = os.fork()
        if child_pid:
        # Родительский процесс, не делаем ничего
            client_sock.close()
            return child_pid

    # Дочерний процесс:
    #  - читаем запрос
    #  - обрабатываем
    #  - записываем ответ
    #  - закрываем сокет
    #  - завершаем процесс (os._exit())
        request = read_request(client_sock) # type: ignore
        if request is None:
            print(f'Client #{cid} unexpectedly disconnected')
        else:
            response = handle_request(request) # type: ignore
            write_response(client_sock, response, cid) # type: ignore
            os._exit(0)

def reap_children(active_children):
    for child_pid in active_children.copy():
        child_pid, _ = os.waitpid(child_pid, os.WNOHANG)
        if child_pid:
            active_children.discard(child_pid)  