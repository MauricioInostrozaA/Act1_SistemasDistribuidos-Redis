# Copyright 2019 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import time

import grpc

import demo_pb2
import demo_pb2_grpc

__all__ = 'simple_method'


SERVER_ADDRESS = "localhost:23333"
CLIENT_ID = 1

# 中文注释和英文翻译
# Note that this example was contributed by an external user using Chinese comments.
# In all cases, the Chinese comment text is translated to English just below it.


# 一元模式(在一次调用中, 客户端只能向服务器传输一次请求数据, 服务器也只能返回一次响应)
# unary-unary(In a single call, the client can only send request once, and the server can
# only respond once.)
def simple_method(stub):
    print("--------------Call SimpleMethod Begin--------------")
    request = demo_pb2.Request(client_id=CLIENT_ID,
                               request_data="called by Python client")
    response = stub.SimpleMethod(request)
    print("resp from server(%d), the message=%s" %
          (response.server_id, response.response_data))
    print("--------------Call SimpleMethod Over---------------")

def main():
    with grpc.insecure_channel(SERVER_ADDRESS) as channel:
        stub = demo_pb2_grpc.GRPCDemoStub(channel)

        simple_method(stub)


if __name__ == '__main__':
    main()
