from pathlib import Path
import json

class Revolution_function:
    def __init__(self) -> None:

        abs_path = Path(__file__).resolve().parent
        with open(Path(abs_path, '../assets', 'FunctionConfig.json'), 'r') as _file:
            self._config = json.load(_file)

        self._a = self._config['a'];
        self._b = self._config['b'];
        self._ring_accuracy = self._config['Ring Accuracy'];
        self._interval_accuracy= self._config['Interval Accuracy'];

    def f_main(self, x):
        return eval(self._config['Function']);
