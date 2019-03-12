#coding utf-8
import json
class op_json:
    def __init__(self,filepath=None):
        if filepath:
            self.filepath = filepath
        else:
            self.filepath = r"D:\学习资料\接口自动化\接口自动化-视频\interfaceauto\interface_autoframe\dataconfig\user.json"
        self.f_data=self.get_json()

    def get_json(self):
        with open(self.filepath,encoding='utf-8') as f:
            data=json.load(f)
        return data

    def get_value(self,key=None):
        #json_file=open(r"D:\学习资料\接口自动化\接口自动化-视频\interfaceauto\interface_autoframe\dataconfig\user.json",encoding="utf-8")
        #json_to_python=json.load(self.f_data)
        if key:
            res_data=self.f_data[key]
        else:
            res_data=None
        return res_data
    def w_json(self,djson,fw=None):
        if fw:
            fw=fw
        else:
            fw=r"D:\学习资料\接口自动化\接口自动化-视频\interfaceauto\interface_autoframe\dataconfig\cookie.json"
        with open(fw,'w') as filew:
            json.dump(djson, filew, ensure_ascii='false', indent=4)

if __name__ == '__main__':
    json_py=op_json(r"D:\学习资料\接口自动化\接口自动化-视频\interfaceauto\interface_autoframe\dataconfig\headers.json")
    print(json_py.get_value('bt_heades'))
    #json_py.w_json({'uid': '0', 'service_id': '1'})


