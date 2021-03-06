import unittest
import shutil
import os
from clockwork import cortex

modules_dir = os.path.dirname(os.path.abspath(cortex.__file__))
data_dir = os.path.join(modules_dir, 'tests', 'data', 'cortex')


class TestCortex(unittest.TestCase):
    def test_run_cortex_run_calls(self):
        '''test run_cortex'''
        ref_dir = os.path.join(data_dir, 'Reference')
        reads_infile = os.path.join(data_dir, 'reads.fq')
        tmp_out = 'tmp.cortex.out'
        sample_name = 'sample_name'
        ctx = cortex.CortexRunCalls(ref_dir, reads_infile, tmp_out, sample_name, mem_height=17)
        ctx.run()

        self.assertTrue(os.path.exists(ctx.cortex_log))
        self.assertEqual(2, len([x for x in os.listdir(os.path.join(tmp_out, 'cortex.out', 'vcfs')) if x.endswith('.vcf')]))
        shutil.rmtree(tmp_out)


    def test_make_run_calls_index_files(self):
        '''test make_run_calls_index_files'''
        ref_fasta = 'tmp.cortex.make_run_calls_index_files.ref.fa'
        outprefix = 'tmp.cortex.make_run_calls_index_files.out'
        expected_suffixes = ['k31.ctx', 'stampy.sthash', 'stampy.stidx']
        expected_files = [outprefix + '.' + x for x in expected_suffixes]
        for filename in expected_files:
            try:
                os.unlink(fielname)
            except:
                pass

        with open(ref_fasta, 'w') as f:
            print('>ref', file=f)
            print('CACTGCTGTGATATTACACGTCGTCTGCAGTCAGTCTGCATGCA', file=f)
            print('TCACTGACTGCATGCATCTGACTGCTACTGT', file=f)

        cortex.make_run_calls_index_files(ref_fasta, outprefix, mem_height=1)
        os.unlink(ref_fasta)

        for filename in expected_files:
            self.assertTrue(os.path.exists(filename))
            os.unlink(filename)

