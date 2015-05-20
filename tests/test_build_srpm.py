from support import RpgTestCase
from rpg import Base
from rpg.command import Command


class BuildSrpmTest(RpgTestCase):
    
    def test_build_srpm(self):

        base = Base()
        base.project_name = Path("/tmp/rpgtest")
        spec_path = test_project_dir / "hellopproject" ...
        arhive_path = test_project_dir / "hellopproject" ...
        base.build_srpm(spec_path, archive_path, base.srpm_path)
        self.assertTrue(base.srpm_path.exists())
        
    def TearDown():
        base = Base()
        Command("rm -r", base.base_dir).execute()

            
