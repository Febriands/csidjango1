from django.db import models

# Create your models here.

class Types(models.Model):
    name = models.CharField(max_length=150)


class Steps(models.Model):
    def save(self, *args, **kwargs):
        if not self.order or self.order == 0:
            last = Steps.objects.filter(types=self.types).order_by('-order').first()
            if last:
                self.order = last.order + 1
            else:
                self.order = 1

        super(Steps, self).save(*args, **kwargs)

    types = models.ForeignKey(Types, on_delete=models.CASCADE)
    order = models.IntegerField(default=0)
    name = models.CharField(max_length=150)


class StepsForms(models.Model):
    steps = models.ForeignKey(Steps, on_delete=models.CASCADE)
    form_type_choices = (
        (0, 'Number'),
        (1, 'Text'),
    )
    form_type = models.IntegerField(choices=form_type_choices, default=1)
    name = models.CharField(max_length=150)


class OfflineDocuments(models.Model):
    steps = models.ForeignKey(Steps, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)


class Certifications(models.Model):
    types = models.ForeignKey(Types, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    completed = models.IntegerField(default=0)
    left = models.IntegerField()
    created = models.BigIntegerField()
    updated = models.BigIntegerField()


class CertificationsSteps(models.Model):
    certifications = models.ForeignKey(Certifications, on_delete=models.CASCADE)
    steps = models.ForeignKey(Steps, on_delete=models.CASCADE)
    validated = models.BooleanField(default=False)
    validator = models.IntegerField(default=None)
    validation_date = models.BigIntegerField(default=None)


class CertificationsDetails(models.Model):
    certifications = models.ForeignKey(Certifications, on_delete=models.CASCADE)
    certifications_steps = models.ForeignKey(CertificationsSteps, on_delete=models.CASCADE)
    steps_forms = models.ForeignKey(StepsForms, on_delete=models.CASCADE)
    value = models.TextField(default=None)


class CertificationsOfflineDocuments(models.Model):
    offline_documents = models.ForeignKey(OfflineDocuments, on_delete=models.CASCADE)
    certifications_steps = models.ForeignKey(CertificationsSteps, on_delete=models.CASCADE)
    files_path = models.CharField(max_length=200, default=None)


class FilesProcessCertifications(models.Model):
    types = models.ForeignKey(Types, on_delete=models.CASCADE)
    certifications = models.ForeignKey(Certifications, on_delete=models.CASCADE)
    files_formulir_aplikasi = models.FileField(upload_to='files_process/', null=True, blank=True)
    files_kelengkapan_dokumen = models.FileField(upload_to='files_process/', null=True, blank=True)
    files_kajian_aplikasi_sertifikasi = models.FileField(upload_to='files_process/', null=True, blank=True)
    files_penawaran = models.FileField(upload_to='files_process/', null=True, blank=True)
    files_perjanjian = models.FileField(upload_to='files_process/', null=True, blank=True)
    files_invoice = models.FileField(upload_to='files_process/', null=True, blank=True)
    files_kuitansi = models.FileField(upload_to='files_process/', null=True, blank=True)
    files_notifikasi_tim_audit_tahap_suv = models.FileField(upload_to='files_process/', null=True, blank=True)
    files_notifikasi_tim_audit_tahap_1 = models.FileField(upload_to='files_process/', null=True, blank=True)
    files_rencana_audit_tahap_suv = models.FileField(upload_to='files_process/', null=True, blank=True)
    files_rencana_audit_tahap_1 = models.FileField(upload_to='files_process/', null=True, blank=True)
    files_audit_kecukupan = models.FileField(upload_to='files_process/', null=True, blank=True)
    files_daftar_hadir_tahap_suv = models.FileField(upload_to='files_process/', null=True, blank=True)
    files_daftar_hadir_tahap_1 = models.FileField(upload_to='files_process/', null=True, blank=True)
    files_laporan_ketidaksesuaian_tahap_suv = models.FileField(upload_to='files_process/', null=True, blank=True)
    files_laporan_ketidaksesuaian_tahap_1 = models.FileField(upload_to='files_process/', null=True, blank=True)
    files_laporan_audit_tahap_suv = models.FileField(upload_to='files_process/', null=True, blank=True)
    files_laporan_audit_tahap_1 = models.FileField(upload_to='files_process/', null=True, blank=True)
    files_verifikasi_ketidaksesuaian_tahap_suv = models.FileField(upload_to='files_process/', null=True, blank=True)
    files_verifikasi_ketidaksesuaian_tahap_1 = models.FileField(upload_to='files_process/', null=True, blank=True)
    files_notifikasi_tim_audit_tahap_2 = models.FileField(upload_to='files_process/', null=True, blank=True)
    files_rencana_audit_tahap_2 = models.FileField(upload_to='files_process/', null=True, blank=True)		
    files_daftar_hadir_tahap_2 = models.FileField(upload_to='files_process/', null=True, blank=True)		
    files_lembar_periksa_audit_suv = models.FileField(upload_to='files_process/', null=True, blank=True)		
    files_lembar_periksa_audit = models.FileField(upload_to='files_process/', null=True, blank=True)		
    files_laporan_ketidaksesuaian_tahap_2 = models.FileField(upload_to='files_process/', null=True, blank=True)		
    files_laporan_audit_tahap_2 = models.FileField(upload_to='files_process/', null=True, blank=True)		
    files_buku_harian_auditor_suv = models.FileField(upload_to='files_process/', null=True, blank=True)		
    files_buku_harian_auditor = models.FileField(upload_to='files_process/', null=True, blank=True)		
    files_pemantauan_lapangan_personnel_sertifikasi_suv = models.FileField(upload_to='files_process/', null=True, blank=True)		
    files_pemantauan_lapangan_personnel_sertifikasi = models.FileField(upload_to='files_process/', null=True, blank=True)		
    files_verifikasi_ketidaksesuaian_tahap_2 = models.FileField(upload_to='files_process/', null=True, blank=True)		
    files_keterangan_bebas_konflik_kepentingan_suv = models.FileField(upload_to='files_process/', null=True, blank=True)		
    files_keterangan_bebas_konflik_kepentingan = models.FileField(upload_to='files_process/', null=True, blank=True)		
    files_notifikasi_tim_evaluasi_suv = models.FileField(upload_to='files_process/', null=True, blank=True)		
    files_notifikasi_tim_evaluasi = models.FileField(upload_to='files_process/', null=True, blank=True)		
    files_laporan_evaluasi_suv = models.FileField(upload_to='files_process/', null=True, blank=True)		
    files_laporan_evaluasi = models.FileField(upload_to='files_process/', null=True, blank=True)		
    files_memo_dinas_hasil_suv = models.FileField(upload_to='files_process/', null=True, blank=True)		
    files_memo_dinas_penerbitan_sertifikat = models.FileField(upload_to='files_process/', null=True, blank=True)		
    files_form_verifikasi_sertifikat = models.FileField(upload_to='files_process/', null=True, blank=True)
    files_draft_sertifikat = models.FileField(upload_to='files_process/', null=True, blank=True)		
    files_sertifikat = models.FileField(upload_to='files_process/', null=True, blank=True)		
    files_program_survailen = models.FileField(upload_to='files_process/', null=True, blank=True)
    
    tahap_1 = {
        '1.1':files_formulir_aplikasi,
        '1.2':files_kelengkapan_dokumen
    }
    tahap_2 = {
        '2.1':files_kajian_aplikasi_sertifikasi,        
    }
    tahap_3 = {
        '3.1':files_penawaran,        
        '3.2':files_perjanjian,        
        '3.3':files_invoice,        
        '3.4':files_kuitansi,        
    }
    tahap_4 = {
        '4.1':files_notifikasi_tim_audit_tahap_1,        
        '4.2':files_rencana_audit_tahap_1,        
        '4.3':files_audit_kecukupan,        
        '4.4':files_daftar_hadir_tahap_1,        
        '4.5':files_laporan_ketidaksesuaian_tahap_1,        
        '4.6':files_laporan_audit_tahap_1,        
        '4.7':files_verifikasi_ketidaksesuaian_tahap_1,        
    }
    tahap_5 = {
        '5.1':files_notifikasi_tim_audit_tahap_2,        
        '5.2':files_rencana_audit_tahap_2,        
        '5.3':files_daftar_hadir_tahap_2,
        '5.4':files_lembar_periksa_audit,                     
        '5.5':files_laporan_ketidaksesuaian_tahap_2,        
        '5.6':files_laporan_audit_tahap_2,        
        '5.7':files_verifikasi_ketidaksesuaian_tahap_2,        
        '5.8':files_buku_harian_auditor,        
        '5.9':files_pemantauan_lapangan_personnel_sertifikasi,        
    }
    tahap_6 = {
        '6.1':files_notifikasi_tim_evaluasi,
        '6.2':files_laporan_evaluasi
    }    
    tahap_7 = {
        '6.1':files_memo_dinas_penerbitan_sertifikat,
        '6.2':files_form_verifikasi_sertifikat,
        '6.3':files_draft_sertifikat,
        '6.4':files_sertifikat,
        '6.5':files_program_survailen
    }    
    tahap_1_suv = {
        '1.1_suv':files_penawaran,             
        '1.2_suv':files_invoice,        
        '1.3_suv':files_kuitansi,        
    }
    tahap_2_suv = {
        '2.1_suv':files_notifikasi_tim_audit_tahap_suv,        
        '2.2_suv':files_rencana_audit_tahap_suv,        
        '2.3_suv':files_daftar_hadir_tahap_suv,
        '2.4_suv':files_lembar_periksa_audit_suv,                     
        '2.5_suv':files_laporan_ketidaksesuaian_tahap_suv,        
        '2.6_suv':files_laporan_audit_tahap_suv,        
        '2.7_suv':files_verifikasi_ketidaksesuaian_tahap_suv,        
        '2.8_suv':files_buku_harian_auditor_suv,        
        '2.9_suv':files_pemantauan_lapangan_personnel_sertifikasi_suv
    }
    tahap_3_suv = {
        '3.1_suv':files_notifikasi_tim_evaluasi_suv,
        '3.2_suv':files_laporan_evaluasi_suv
    }    
    tahap_4_suv = {
        '4.1_suv':files_memo_dinas_hasil_suv,       
    }          