import shutil
import sys
import tempfile
import os

from networkml.featurizers.csv_to_features import CSVToFeatures
from networkml.parsers.pcap_to_csv import PCAPToCSV

C2FARGS = ['csv_to_features.py', '-c', '-g', 'host_tshark']


def test_CSVToFeatures():
    with tempfile.TemporaryDirectory() as tmpdir:
        sys.argv = ['pcap_to_csv.py', '-e', 'tshark', '-o', os.path.join(tmpdir, 'foo-1.csv.gz'),
                    './tests/test_data/trace_ab12_2001-01-01_02_03-client-ip-1-2-3-4.pcap']
        instance = PCAPToCSV()
        instance.main()
        sys.argv = C2FARGS + [
            '-o', os.path.join(tmpdir, 'combined.csv.gz'), os.path.join(tmpdir, 'foo-1.csv.gz')]
        instance2 = CSVToFeatures()
        instance2.main()


def test_CSVToFeatures_no_output():
    with tempfile.TemporaryDirectory() as tmpdir:
        testdata = os.path.join(tmpdir, 'test_data')
        shutil.copytree('./tests/test_data', testdata)
        sys.argv = ['pcap_to_csv.py', '-e', 'tshark', os.path.join(testdata, 'trace_ab12_2001-01-01_02_03-client-ip6-1-2-3-4.pcap')]
        instance = PCAPToCSV()
        instance.main()
        sys.argv = C2FARGS + [os.path.join(testdata, 'trace_ab12_2001-01-01_02_03-client-ip6-1-2-3-4.pcap.csv.gz')]
        instance2 = CSVToFeatures()
        instance2.main()


def test_CSVToFeatures_no_group_or_func():
    with tempfile.TemporaryDirectory() as tmpdir:
        testdata = os.path.join(tmpdir, 'test_data')
        shutil.copytree('./tests/test_data', testdata)
        sys.argv = ['csv_to_features.py', '-g', '', os.path.join(testdata, 'trace_ab12_2001-01-01_02_03-client-ip-1-2-3-4.pcap.csv.gz')]
        instance = CSVToFeatures()
        instance.main()


def test_CSVToFeatures_dir():
    with tempfile.TemporaryDirectory() as tmpdir:
        sys.argv = ['pcap_to_csv.py', '-e', 'tshark', '-o', os.path.join(tmpdir, 'foo2'), './tests']
        instance = PCAPToCSV()
        instance.main()
        sys.argv = C2FARGS + ['-t', '2', os.path.join(tmpdir, 'foo2')]
        instance2 = CSVToFeatures()
        instance2.main()


def test_CSVToFeatures_dir_output():
    with tempfile.TemporaryDirectory() as tmpdir:
        foo2 = os.path.join(tmpdir, 'foo2')
        foo2out = os.path.join(tmpdir, 'foo2_output')
        sys.argv = ['pcap_to_csv.py', '-e', 'tshark', '-o', foo2, './tests']
        instance = PCAPToCSV()
        instance.main()
        sys.argv = C2FARGS + ['-t', '2', '-o', foo2out, foo2]
        instance2 = CSVToFeatures()
        instance2.main()


def test_CSVToFeatures_host():
    with tempfile.TemporaryDirectory() as tmpdir:
        foo3 = os.path.join(tmpdir, 'foo3')
        sys.argv = ['pcap_to_csv.py', '-e', 'tshark', '-o', foo3, './tests']
        instance = PCAPToCSV()
        instance.main()
        sys.argv = ['csv_to_features.py', '-c', '-z', 'input', '-g', 'sessionhost_tshark', foo3]
        instance2 = CSVToFeatures()
        instance2.main()