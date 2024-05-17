# ПО для снятия показаний с интерфейса WiLab от CMA-Science

[WiLab Product page](https://cma-science.nl/wilab_en)

## Требования

- Linux
    - нужно дать пользователю доступ к USB, либо запускать от root
- Python 11

## Установка

```shell
git clone https://github.com/BardinPetr/wilab-datalogger
cd wilab-datalogger
pip install -r requirements.txt
./start.sh
```

Чтобы прописать доступ к конкретно данному USB устройству, воспользуемся UDEV.

```shell
sudo cp ./20-wilab.rules /etc/udev/rules.d/20-wilab.rules
sudo udevadm control --reload-rules
```
