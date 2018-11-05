# coding=utf-8
import PyHook3
import pythoncom
FileName = 'mouse_log.txt'
mouse_window_name = None

def onMouseEvent(event):
    # print('MessageName:', event.MessageName)
    # print('Message:', event.Message)
    # print('Time:', event.Time)
    # print('Window:', event.Window)
    # print('WindowName:', event.WindowName)
    # print('Position:', event.Position)
    # print('Wheel:', event.Wheel)
    # print('Injected:', event.Injected)
    # print('---')

    # 监听鼠标事件
    print(event.Position)
    result = '%s %s\n' % event.Position
    with open(FileName, 'ab+') as f:
        f.writelines(result)
        # 需要注意的是返回True，以便将事件传给其他的处理程序，如果返回False，鼠标事件在这里就会被拦截，鼠标会将僵在此处失去响应

    # 使信息继续传递
    return True

def main():
    # 1.创建钩子管理器
    hm = PyHook3.HookManager()
    # 2.监听到目标事件，回调函数
    hm.MouseAll = onMouseEvent

    # 3.监听事件（按键事件）
    hm.HookMouse()

    # 4.善后处理，消息顺利传递
    pythoncom.PumpMessages()

if __name__ == '__main__':
    main()