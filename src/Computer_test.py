from unittest import TestCase
from unittest.mock import patch
from subprocess import CalledProcessError
import Computer
import re

class ComputerTest(TestCase):

    @patch('Computer.check_output')
    def test_sophos_service_not_installed(self, mock_check_output):
        mock_check_output.side_effect = CalledProcessError(returncode = 1, cmd = 'sophos not installed')

        sophos = Computer.get_sophos_status()
        self.assertEqual(sophos, {
            "is_installed": "false",
            "is_running": "false"
        })

    @patch('Computer.check_output')
    def test_sophos_service_is_installed(self, mock_check_output):
        sc_query_output=b'''
        SERVICE_NAME: SAVService
        TYPE               : 10  WIN32_OWN_PROCESS
        STATE              : 4  RUNNING
                                (STOPPABLE, NOT_PAUSABLE, IGNORES_SHUTDOWN)
        WIN32_EXIT_CODE    : 0  (0x0)
        SERVICE_EXIT_CODE  : 0  (0x0)
        CHECKPOINT         : 0x0
        WAIT_HINT          : 0x0
        '''
        mock_check_output.return_value = sc_query_output

        sophos = Computer.get_sophos_status()
        
        self.assertEqual(sophos, {
            "is_installed": "true",
            "is_running": "true"
        })
   
   
    @patch('Computer.check_output')
    def test_sophos_service_is_installed_but_not_running(self, mock_check_output):
        sc_query_output=b'''
        SERVICE_NAME: SAVService
        TYPE               : 10  WIN32_OWN_PROCESS
        STATE              : 1  STOPPED
                                (STOPPABLE, NOT_PAUSABLE, IGNORES_SHUTDOWN)
        WIN32_EXIT_CODE    : 0  (0x0)
        SERVICE_EXIT_CODE  : 0  (0x0)
        CHECKPOINT         : 0x0
        WAIT_HINT          : 0x0
        '''
        mock_check_output.return_value = sc_query_output

        sophos = Computer.get_sophos_status()
        
        self.assertEqual(sophos, {
            "is_installed": "true",
            "is_running": "false"
        })





