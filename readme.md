#  habraproxy.py � ��� ���������� http-������-������, ����������� �������� (���� �� ���� 
#  ����������), ������� ���������� ���������� ������� �����. � ����� �����������: �����  
#  ������� ����� �� ����� ���� ������ ������ ������ ���. �������� ���:
#
#  http://habrahabr.ru/company/yandex/blog/258673/
#  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#  ������ �� ���� ���������� Logjam ��� � ��������� � ��������� ��� ��������� �������� � 
#  ����������� TLS. � ���� ��������������� ���� ������������, ����� ���������� �� ����� �� 
#  ���, � ������ � � ��������� ciphersiutes.
#
#  http://127.0.0.1:8232/company/yandex/blog/258673/
#  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#  ������ �� ���� ���������� Logjam� ��� � ��������� � ��������� ��� ��������� �������� � 
#  ����������� TLS. � ���� ��������������� ���� ������������, ����� ���������� �� ����� �� 
#  ���, � ������ � � ��������� ciphersiutes. 
#
#  �������:
#    * Python 2.x
#    * ����� ������������ ����� ������������� ����������, ������� ������ ������
#    * ��� ������ ����, ��� �����. PEP8 � �����������
#    * � ������, ���� �� ������� �����-�� ������, ������� ��������� �� ������� �����
#
#  ���� ������ ������� ������ �������, ����� �������� ���������:
#    * ��������� ��������� ������ (����, ����, ����, �������� �� ����� � �.�.)
#    * ����� ������ ���������� ������� ������������� ����������� ������� � �������� 
#      ������������ ������� ���������
 
 
 libs:
    gzip
    re
    urllib2
    bs4
    StringIO