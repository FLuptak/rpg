from support import RpgTestCase
from rpg import Base
from rpg.command import Command


class BuildSrpmTest(RpgTestCase):
    
    def test_build_srpm(self):
        base = Base()
        base.load_plugins()
        base.process_archive_or_dir(
            self.test_project_dir / "hello_project/hello-1.4.tar.gz")
        base.spec.Name = "hello"
        base.spec.Version = "1.4"
        base.spec.Release = "1%{?dist}"
        base.spec.License = "GPLv2"
        base.spec.Summary = "Hello World test program"
        base.spec.description = "Hello World C project for testing RPG."
        base.spec.build = "make"
        base.spec.install = "make install DESTDIR=%{RPM_BUILD_ROOT}"
        base.run_raw_sources_analysis()
        base.run_patched_sources_analysis()
        base.write_spec()
        base._package_builder.build_srpm(base.spec_path, base.archive_path, base.base_dir)
        self.assertTrue(base.srpm_path.exists())
        
    def TearDown():
        base = Base()
        Command("rm -r", base.base_dir).execute()

            
