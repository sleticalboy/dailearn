import time

from scrapy.exporters import BaseItemExporter


# 自定义数据导出
class TxtExporter(BaseItemExporter):

    def __init__(self, file, **kwargs):
        super().__init__(**kwargs)
        print(f'TxtExporter() file: {file}')
        if isinstance(file, str):
            file = open(file, 'wb', encoding='utf-8', newline='\n')
        self._fp = file

    def start_exporting(self):
        self._fp.write(f'# auto added by TxtExporter {time.time()}'.encode())
        pass

    def export_item(self, item):
        data = '\t'.join(dict(self._get_serialized_fields(item)).values()) + '\n'
        self._fp.write(data.encode())
        print(f'export_item() {data}')
        pass

    def finish_exporting(self):
        self._fp.close()
        pass
