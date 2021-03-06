from rpg.package_builder import PackageBuilder
from tests.support import RpgTestCase
from rpg.command import Command


class PackageBuilderTest(RpgTestCase):

    @classmethod
    def setUpClass(cls):
        cls.distro = "fedora-22"
        cls.arch = "x86_64"
        cls.package_builder = PackageBuilder()
        cls.package_builder.fetch_repos(cls.distro, cls.arch)

    def setUp(self):
        self.srpm = RpgTestCase.test_project_dir / "srpm"
        self.fail_srpm = self.srpm / "fail.src.rpm"
        self.test_srpm = self.srpm / "test.src.rpm"

    def test_build_rpm(self):
        self.assertEqual(
            self.package_builder.build_rpm(self.test_srpm,
                                           PackageBuilderTest.distro,
                                           PackageBuilderTest.arch),
            [])

    def test_build_rpm_fail(self):
        self.assertNotEqual(
            self.package_builder.build_rpm(self.fail_srpm,
                                           PackageBuilderTest.distro,
                                           PackageBuilderTest.arch),
            [])

    def tearDown(self):
        Command("rm -rf " + str(self.srpm) + "/*.log").execute()
        Command("rm -rf " + str(self.srpm) + "/a-a-a.src.rpm").execute()
